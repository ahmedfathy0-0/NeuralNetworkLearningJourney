import numpy as np
from typing import Union

class PCA():
    def __init__(self,  new_dim: Union[int, float]) -> None:
        # hyperparameter representing the number of dimensions after reduction
        # (or variance threshold if it's a float between 0 and 1)
        self.new_dim = new_dim
        # for standardization
        self.μ:np.ndarray
        self.σ:np.ndarray
        # for PCA
        self.A:np.ndarray 

    # x_train is (m,n) matrix where each row is an n-dimensional vector of features
    def fit(self, x_train):
        # TODO 1: Find μ and σ of each feature in x_train
        self.μ = np.mean(x_train, axis=0)
        self.σ = np.std(x_train, axis=0)
        # if a column has zero std (useless constant) set σ=1 (skip their standardization)
        self.σ = np.where(self.σ == 0, 1, self.σ)
        
        # TODO 2: Standardize the training data
        z_train = (x_train - self.μ) / self.σ
                
        # TODO 3: Compute SVD on z_train instead of eigendecomposition of covariance
        # SVD: z_train = U @ np.diag(S) @ Vh
        U, S, Vh = np.linalg.svd(z_train, full_matrices=False)
        
        # The variances (eigenvalues of covariance matrix) are S**2 / m
        m = z_train.shape[0]
        λs = (S ** 2) / m
        
        # Note: np.linalg.svd already returns singular values (and corresponding vectors) sorted in descending order
        
        # TODO 4: Determine the number of components L
        if isinstance(self.new_dim, float) and 0.0 < self.new_dim < 1.0:
            var_ratios = np.cumsum(λs) / np.sum(λs)
            # Find the number of components such that the cumulative variance ratio is at least new_dim
            L = np.argmax(var_ratios >= self.new_dim) + 1
        else:
            L = int(self.new_dim)
        
        # TODO 5: Select the top L eigenvectors and set A accordingly
        # Vh contains the principal components as rows, already sorted
        self.A = Vh[:L, :]
        
        return self
    
    # x_val is (m,n) matrix where each row is an n-dimensional vector of features
    def transform(self, x_val):
        z_val = (x_val - self.μ) / self.σ
        # TODO 6: Apply the transformation equation
        return z_val @ self.A.T
    
    def inverse_transform(self, z_val):
        # TODO 7: Apply the inverse transformation equation (including destandardization)
        x_reconstructed = z_val @ self.A
        return x_reconstructed * self.σ + self.μ

    def fit_transform(self, x_train):
        return self.fit(x_train).transform(x_train)
