# Необходимо реализовать метод разворота связного списка 
# (двухсвязного или односвязного на выбор).

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        current_value = self.head
        while current_value is not None:
            print (current_value.value)
            current_value = current_value.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Функция разворота связного списка
def reversal_linked_list(linked_list):
    current = linked_list.head # Текущее значение (ссылка на head)
    previous = None   # Ссылка на предыдущий элемент
    next_node = None  # Ссылка на следующий элемент
    # Цикл пока мы не достигли конца списка (next == None)
    while current:
        # next_node присваиваем ссылку на следующий элемент
        next_node = current.next
        # Текущему полю next присваиваем ссылку на предыдущий элемент
        current.next = previous
        # Переменной previous присваиваем текущую ссылку
        previous = current
        # Переменной new_head присваиваем значение текущего узла
        new_head = current
        # и следующий узел становится текущим узлом, на который мы смотрим
        current = next_node
    
    # Полю head присваиваем значение последнего текущего узла
    linked_list.head = new_head
    return linked_list


list = LinkedList()
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
node4 = Node("Thursday")
list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

print("Сформированный первичный связный список:")
list.print_linked_list()
print("--------------------------------")

# Вызов функции разворота связного списка
reversal_linked_list(list)

print("Развернутый связный список:")
list.print_linked_list()