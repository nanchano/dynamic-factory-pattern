# Dynamic Factory Design Pattern

The factory pattern might be one of the most common and well known design patterns, and for good reasons. It relies on abstractions while being able to serve clients with concrete implementations of the object they want.

Usually, the pattern relies on `if` or `switch/match` chains to determine the object to return, which can work when there are a limited number of objects, but it presents some problems when scaling, as forgetting to add the condition to the factory ends up creating unexpected side effects.

An alternative is just making a dynamic factory, which sacrificies readability for scalability, while also introducing some conditions in the way the project, modules and objects should be structure or named.

It's especially easy to implement in Python by leveraging the `getattr` function and the `importlib` module, as we can dynamically look for objects in any module we want.

For a walkthrough of the example, head to my [blog post](https://wwww.sharkie.dev/dynamic-factory-pattern) 
