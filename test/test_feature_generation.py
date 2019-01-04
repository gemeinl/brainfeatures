import numpy as np

from brainfeatures.feature_generation.generate_features import \
    generate_features_of_one_file


def test_generate_features():
    signals = np.random.rand(2*1000).reshape(2, 1000)
    feature_df = generate_features_of_one_file(signals, 100, 2, 1, "boxcar",
                                               [[0, 2], [2, 4], [4, 8]],
                                               ["a", "b"], "median", "db4",
                                               "morl", True)
    assert len(feature_df) == 1

    feature_df = generate_features_of_one_file(signals, 100, 2, 1, "boxcar",
                                               [[0, 2], [2, 4], [4, 8]],
                                               ["a", "b"], "none", "db4",
                                               "morl", True)
    assert len(feature_df) == 5
