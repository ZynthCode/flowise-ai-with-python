Dependency Injection is a design pattern commonly used in software development to implement loose coupling between components or classes. It allows the dependencies of a class to be provided from the outside, rather than being created within the class itself. This promotes code reusability, testability, and flexibility.

In Java, one popular framework for implementing Dependency Injection is Spring Framework. Spring provides a feature called "Inversion of Control" (IoC) container, which manages the creation and injection of dependencies.

Here's an example of how Dependency Injection can be implemented using Spring Framework:

1. Define a class that has a dependency:

```java
public class UserService {
    private UserRepository userRepository;

    // Constructor Injection
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    // Business logic methods
    public void addUser(User user) {
        userRepository.save(user);
    }
}
```

2. Define the dependency interface:

```java
public interface UserRepository {
    void save(User user);
}
```

3. Implement the dependency interface:

```java
@Repository
public class UserRepositoryImpl implements UserRepository {
    public void save(User user) {
        // Implementation to save user to a database
    }
}
```

4. Configure the dependencies in a Spring configuration file:

```java
@Configuration
public class AppConfig {
    @Bean
    public UserRepository userRepository() {
        return new UserRepositoryImpl();
    }

    @Bean
    public UserService userService(UserRepository userRepository) {
        return new UserService(userRepository);
    }
}
```

5. Use the dependency in the main application:

```java
public class MainApplication {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        UserService userService = context.getBean(UserService.class);
        
        User user = new User("John Doe");
        userService.addUser(user);
    }
}
```

In this example, the `UserService` class has a dependency on the `UserRepository` interface. The dependency is provided through constructor injection in the `UserService` constructor. The actual implementation of the `UserRepository` interface is defined in the `UserRepositoryImpl` class, which is annotated with `@Repository` to indicate that it is a Spring-managed bean.

The dependencies are configured in the `AppConfig` class using the `@Bean` annotation. The `userRepository()` method defines the bean for the `UserRepository` implementation, and the `userService()` method defines the bean for the `UserService` class, injecting the `userRepository` bean as a parameter.

Finally, in the `MainApplication` class, the Spring IoC container is initialized with the `AppConfig` class, and the `UserService` bean is obtained from the container. The `UserService` methods can then be called, and the dependency is automatically injected by the Spring framework.

This is a basic example of Dependency Injection using Spring Framework. There are additional features and annotations provided by Spring that can be used to control the scope and lifecycle of dependencies, as well as to enable more advanced dependency injection scenarios.