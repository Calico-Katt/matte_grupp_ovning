#Kod jag hittade på wiki om Power iteration
import numpy as np

def power_iteration(A, num_iterations: int):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.random.rand(A.shape[1])

    for _ in range(num_iterations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm

    return b_k

print(power_iteration(np.array([[0.5, 0.5], [0.2, 0.8]]), 10))


#Denna äkliga kod dök upp på wiki om Rayleigh quotient iteration
"""
def rayleigh(A, epsilon, mu, x)
  x = x / norm(x);
  % the backslash operator in Octave solves a linear system
  y = (A - mu * eye(rows(A))) \ x; 
  lambda = y' * x;
  mu = mu + 1 / lambda
  err = norm(y - lambda * x) / norm(y)

  while err > epsilon
    x = y / norm(y);
    y = (A - mu * eye(rows(A))) \ x;
    lambda = y' * x;
    mu = mu + 1 / lambda
    err = norm(y - lambda * x) / norm(y)
  end

end
"""