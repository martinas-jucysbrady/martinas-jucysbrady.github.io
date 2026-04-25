# import libraries
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

np.random.seed(42)

# load dataset
DATASET_PATH = r"D:\ML dataset"
IMG_SIZE = 128
CLASSES = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

def load_images(data_dir):
    images = []
    labels = []
    for class_name in CLASSES:
        class_path = os.path.join(data_dir, class_name)
        for img_name in os.listdir(class_path):
            if img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                img = Image.open(os.path.join(class_path, img_name)).convert('RGB')
                img = img.resize((IMG_SIZE, IMG_SIZE))
                images.append(np.array(img))
                labels.append(class_name)
    return np.array(images), np.array(labels)

X_train_raw, y_train_raw = load_images(os.path.join(DATASET_PATH, 'Training'))
X_test_raw, y_test_raw = load_images(os.path.join(DATASET_PATH, 'Testing'))
print(f"train: {X_train_raw.shape}, test: {X_test_raw.shape}")

# preprocessing
le = LabelEncoder()
y_train = le.fit_transform(y_train_raw)
y_test = le.transform(y_test_raw)

# normalise and flatten
X_train_flat = (X_train_raw.astype('float32') / 255.0).reshape(len(X_train_raw), -1)
X_test_flat = (X_test_raw.astype('float32') / 255.0).reshape(len(X_test_raw), -1)

# scale and apply PCA
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_flat)
X_test_scaled = scaler.transform(X_test_flat)

pca = PCA(n_components=0.95, random_state=42)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
print(f"PCA: {X_train_flat.shape[1]} -> {X_train_pca.shape[1]} components")

# train classifiers
svm = SVC(kernel='rbf', C=10, gamma='scale', probability=True, random_state=42)
rf = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42)
knn = KNeighborsClassifier(n_neighbors=7, weights='distance')
nb = GaussianNB()

classifiers = {'SVM': svm, 'Random Forest': rf, 'KNN': knn, 'Naive Bayes': nb}
predictions = {}

for name, clf in classifiers.items():
    clf.fit(X_train_pca, y_train)
    predictions[name] = clf.predict(X_test_pca)
    print(f"{name}: {accuracy_score(y_test, predictions[name]):.4f}")

# ensemble with all 4
ens4 = VotingClassifier(estimators=list(classifiers.items()), voting='soft')
ens4.fit(X_train_pca, y_train)
predictions['Ensemble (4-model)'] = ens4.predict(X_test_pca)
print(f"Ensemble (4-model): {accuracy_score(y_test, predictions['Ensemble (4-model)']):.4f}")

# ensemble without nb
ens3 = VotingClassifier(estimators=[('SVM', svm), ('Random Forest', rf), ('KNN', knn)], voting='soft')
ens3.fit(X_train_pca, y_train)
predictions['Ensemble (SVM+RF+KNN)'] = ens3.predict(X_test_pca)
print(f"Ensemble (SVM+RF+KNN): {accuracy_score(y_test, predictions['Ensemble (SVM+RF+KNN)']):.4f}")

# results table
print(f"\n{'Model':<25} {'Acc':<8} {'Prec':<8} {'Rec':<8} {'F1':<8}")
for name, pred in predictions.items():
    print(f"{name:<25} {accuracy_score(y_test, pred):<8.4f} {precision_score(y_test, pred, average='weighted'):<8.4f} {recall_score(y_test, pred, average='weighted'):<8.4f} {f1_score(y_test, pred, average='weighted'):<8.4f}")

# detailed report for best ensemble
print(classification_report(y_test, predictions['Ensemble (SVM+RF+KNN)'], target_names=le.classes_))

# confusion matrixes
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
for i, (name, pred) in enumerate(predictions.items()):
    ax = axes.flatten()[i]
    sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt='d', cmap='Blues',
                xticklabels=le.classes_, yticklabels=le.classes_, ax=ax, cbar=False)
    ax.set_title(f'{name} ({accuracy_score(y_test, pred):.3f})')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
axes.flatten()[5].set_visible(False)
plt.tight_layout()
plt.show()

# bar chart comparison
fig, ax = plt.subplots(figsize=(12, 6))
models = list(predictions.keys())
x = np.arange(len(models))
w = 0.18
for i, (metric, fn) in enumerate([('Accuracy', accuracy_score), ('Precision', lambda y,p: precision_score(y,p,average='weighted')), ('Recall', lambda y,p: recall_score(y,p,average='weighted')), ('F1', lambda y,p: f1_score(y,p,average='weighted'))]):
    vals = [fn(y_test, predictions[m]) for m in models]
    ax.bar(x + i*w, vals, w, label=metric)
ax.set_xticks(x + 1.5*w)
ax.set_xticklabels(models, rotation=10, ha='right')
ax.set_ylim(0, 1.05)
ax.legend()
ax.set_title('Model Comparison')
plt.tight_layout()
plt.show()

# PCA variance plot
plt.figure(figsize=(8, 5))
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.axhline(y=0.95, color='r', linestyle='--', label='95%')
plt.xlabel('Components')
plt.ylabel('Cumulative Variance')
plt.title('PCA Explained Variance')
plt.legend()
plt.tight_layout()
plt.show()

# Sample MRI images
fig, axes = plt.subplots(4, 4, figsize=(14, 12))
for i, cls in enumerate(CLASSES):
    idx = np.where(y_train_raw == cls)[0]
    samples = np.random.choice(idx, 4, replace=False)
    for j in range(4):
        axes[i, j].imshow(X_train_raw[samples[j]])
        axes[i, j].axis('off')
labels = ['Glioma', 'Meningioma', 'No Tumour', 'Pituitary']
for i, label in enumerate(labels):
    fig.text(0.02, 0.82 - (i * 0.235), label, fontsize=13, fontweight='bold', va='center')

plt.suptitle('Sample MRI Images by Tumour Type', fontsize=14, fontweight='bold')
plt.subplots_adjust(left=0.15)
plt.show()

# Tumour type distribution bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
classes, counts = np.unique(y_train_raw, return_counts=True)
ax1.bar(classes, counts, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
ax1.set_title('Training Set')
ax1.set_ylabel('Count')
for i, c in enumerate(counts):
    ax1.text(i, c + 10, str(c), ha='center')

classes_t, counts_t = np.unique(y_test_raw, return_counts=True)
ax2.bar(classes_t, counts_t, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
ax2.set_title('Testing Set')
for i, c in enumerate(counts_t):
    ax2.text(i, c + 2, str(c), ha='center')
plt.tight_layout()
plt.show()