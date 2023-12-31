import unittest

import rllib_simple_q.simple_q.simple_q as simple_q

import ray
from ray.rllib.examples.env.deterministic_envs import create_cartpole_deterministic
from ray.rllib.utils.test_utils import check_reproducibilty
from ray.tune import register_env


class TestReproSimpleQ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ray.init()

    @classmethod
    def tearDownClass(cls):
        ray.shutdown()

    def test_reproducibility_dqn_cartpole(self):
        """Tests whether the algorithm is reproducible within 3 iterations
        on discrete env cartpole."""

        register_env("DeterministicCartPole-v1", create_cartpole_deterministic)
        config = simple_q.SimpleQConfig().environment(
            env="DeterministicCartPole-v1", env_config={"seed": 42}
        )
        check_reproducibilty(
            algo_class=simple_q.SimpleQ,
            algo_config=config,
            fw_kwargs={"frameworks": ("tf", "torch")},
            training_iteration=3,
        )


if __name__ == "__main__":
    import sys

    import pytest

    sys.exit(pytest.main(["-v", __file__]))
