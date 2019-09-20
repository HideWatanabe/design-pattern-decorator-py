# Decorator

## Definição do GoF, no livro "Padrões de Projeto" (2000)

### Intenção:
Dinamicamente, agregar responsabilidades adicionais a um objeto. Os **Decorators** fornecem uma alternativa flexível ao
uso de subclasses para extensão de funcionalidades

### Tipo de pattern:
Estrutural

### Também conhecido como:
Wrapper

### Aplicável quando:
- Para acrescentar responsabilidades a objetos individuais de forma dinâmica e transparente, ou seja, sem afetar outros
objetos
- Para responsabilidades que podem ser removidas
- Quando a extensão através do uso de subclasses não é prática. Às vezes, um grande número de extensões independentes é 
possível e isso poderia produzir uma explosão de subclasses para suportar cada combinação. Ou a definição de uma classe 
pode estar oculta ou não estar disponível para a utilização de subclasses.

### Participantes:
- **Component:** Define a interface para objetos que podem ter responsabilidades acrescentadas aos mesmos dinamicamente.
- **ConcreteComponent:** Define um objeto para o qual responsabilidades adicionais podem ser atribuídas
- **Decorator:** Mantém uma referência para um objeto **Component** e define uma interface que segue a interface do 
**Component**
- **ConcreteDecorator:** Acrescenta responsabilidades ao componente