# TD-0-Prediction
Tabular based TD(0) Prediction algorithm.



# Usage
```
    algorithm = TD0Prediction(env=env, policy=policy, alpha=0.1, gamma=0.9)

    V = algorithm.predict(num_episodes=100)
```

1. ``env`` should be a gymnasium environment.
2. ```policy``` can be any function that takes an observation as input and outputs an action (not action probabilities).
3. ```alpha``` is the step-size.
4. ```gamma``` is the discount factor.


See example usage in the ```random_walk_test.py``` module. The random walk example is inspired from _Example 6.2 Random Walk_ in _Chapter 6_ of the book: _Reinforcement Learning An Introduction (2nd Ed)_ by _Sutton_ & _Barto_.
