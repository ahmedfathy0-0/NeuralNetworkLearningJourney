import numpy as np
from Hypothesis import HypothesisFunction

def test():
    try:
        # Initialization
        hypothesis_function = HypothesisFunction(300, 200, 100)
        
        # Assertion 1
        assert hypothesis_function.l == 300
        assert hypothesis_function.m == 200
        assert hypothesis_function.k == 100
        print("Assertion 1 passed")

        # Assertion 2
        assert hypothesis_function.Wh.shape == (200, 300)
        assert hypothesis_function.Wo.shape == (100, 200)
        assert np.allclose(np.mean(hypothesis_function.Wh), 0, atol=1e-1)
        assert np.allclose(np.mean(hypothesis_function.Wo), 0, atol=1e-1)
        assert np.allclose(np.std(hypothesis_function.Wh), 1, atol=1e-1)
        assert np.allclose(np.std(hypothesis_function.Wo), 1, atol=1e-1)
        print("Assertion 2 passed")

        # Assertion 3
        assert np.all(hypothesis_function.bo == 0)
        assert np.all(hypothesis_function.bh == 0)
        print("Assertion 3 passed")

        # Assertion 4
        x = np.arange(300).reshape(-1, 1)
        y, a = hypothesis_function.forward(x)
        assert a.shape == (200, 1)
        print("Assertion 4 passed")

        # Assertion 5
        assert np.all(y >= 0)
        print("Assertion 5 passed")

        # Assertion 6
        x1 = np.arange(300).reshape(-1, 1)
        x2 = np.arange(300).reshape(-1, 1)
        z_bar = hypothesis_function.double_forward(x1, x2)
        assert z_bar.shape == (200, 1)
        print("Assertion 6 passed")

        # Assertion 7
        # Note: z_bar might have small numerical noise, checking mean 0 and std 1
        print(f"Mean: {z_bar.mean()}, Std: {z_bar.std()}")
        assert np.allclose(z_bar.mean(), 0, atol=1e-2)
        assert np.allclose(z_bar.std(), 1, atol=1e-2)
        print("Assertion 7 passed")

        # Assertion 8
        assert hypothesis_function.count_params() == 300*200 + 200*100 + 100 + 200
        print("Assertion 8 passed")
        
        print("All tests passed successfully!")

    except AssertionError as e:
        print(f"Test failed: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    test()
