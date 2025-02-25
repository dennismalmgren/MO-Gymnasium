![tests](https://github.com/Farama-Foundation/mo-gymnasium/workflows/Python%20tests/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# MO-Gymnasium: Multi-Objective Reinforcement Learning Environments

<!-- start elevator-pitch -->

MO-Gymnasium is an open source Python library for developing and comparing multi-objective reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API. Essentially, the environments follow the standard [Gymnasium API](https://github.com/Farama-Foundation/Gymnasium), but return vectorized rewards as numpy arrays.

The documentation website is at [mo-gymnasium.farama.org](https://mo-gymnasium.farama.org), and we have a public discord server (which we also use to coordinate development work) that you can join here: https://discord.gg/bnJ6kubTg6.

<!-- end elevator-pitch -->

## Environments

MO-Gymnasium includes environments taken from the MORL literature, as well as multi-objective version of classical environments, such as MuJoco.
The full list of environments is available [here](https://mo-gymnasium.farama.org/environments/all-environments/).

## Installation
<!-- start install -->

To install MO-Gymnasium, use:
```bash
pip install mo-gymnasium
```

This does not include dependencies for all families of environments (some can be problematic to install on certain systems). You can install these dependencies for one family like `pip install "mo-gymnasium[mujoco]"` or use `pip install "mo-gymnasium[all]"` to install all dependencies.

<!-- end install -->

## API

<!-- start snippet-usage -->

As for Gymnasium, the MO-Gymnasium API models environments as simple Python `env` classes. Creating environment instances and interacting with them is very simple - here's an example using the "minecart-v0" environment:

```python
import gymnasium as gym
import mo_gymnasium as mo_gym
import numpy as np

# It follows the original Gymnasium API ...
env = mo_gym.make('minecart-v0')

obs, info = env.reset()
# but vector_reward is a numpy array!
next_obs, vector_reward, terminated, truncated, info = env.step(your_agent.act(obs))

# Optionally, you can scalarize the reward function with the LinearReward wrapper
env = mo_gym.LinearReward(env, weight=np.array([0.8, 0.2, 0.2]))
```
For details on multi-objective MDP's (MOMDP's) and other MORL definitions, see [A practical guide to multi-objective reinforcement learning and planning](https://link.springer.com/article/10.1007/s10458-022-09552-y).

You can also check more examples in this colab notebook! [![MO-Gym Demo in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Farama-Foundation/MO-Gymnasium/blob/main/mo_gymnasium_demo.ipynb)

<!-- end snippet-usage -->

## Notable related libraries

[MORL-Baselines](https://github.com/LucasAlegre/morl-baselines) is a repository containing various implementations of MORL algorithms by the same authors as MO-Gymnasium. It relies on the MO-Gymnasium API and shows various examples of the usage of wrappers and environments.

## Environment Versioning

MO-Gymnasium keeps strict versioning for reproducibility reasons. All environments end in a suffix like "-v0".  When changes are made to environments that might impact learning results, the number is increased by one to prevent potential confusion.

## Citing

<!-- start citation -->

If you use this repository in your work, please cite:

```bibtex
@inproceedings{Alegre+2022bnaic,
  author = {Lucas N. Alegre and Florian	Felten and El-Ghazali Talbi and Gr{\'e}goire Danoy and Ann Now{\'e} and Ana L. C. Bazzan and Bruno C. da Silva},
  title = {{MO-Gym}: A Library of Multi-Objective Reinforcement Learning Environments},
  booktitle = {Proceedings of the 34th Benelux Conference on Artificial Intelligence BNAIC/Benelearn 2022},
  year = {2022}
}
```

<!-- end citation -->
