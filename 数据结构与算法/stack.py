#列表实现栈

class Stack(object):
    '''栈'''
    def __init__(self):
        self.__list =[]

    def push(self,item):
        '''添加一个元素到栈顶'''
        self.__list.append(item)

    def pop(self):
        '''弹出栈顶元素'''
        return self.__list.pop()


    def peek(self):
        '''返回栈顶元素'''
        if self.__list :
            return self.__list[-1]
        else :
            return None

    def is_empty(self):
        '''判断栈是否为空'''
        return self.__list ==[]

    def size(self):
        '''返回栈元素个数'''
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()