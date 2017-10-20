/* ������ ������ ���������� � ���� � ����� ���� ���� �������� ���-������. 
� ���� ������ ��� ����� �������� ���� ���������� ���������� ������� (������ ��� py3) min � max. 
��������� ���������� ������� ������������� �����: import, eval, exec, globals. 
�� ��������, ��� � ���� ������ ��� ����� ����������� ��� �������, � �� ���� ��� ������.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

���������� ���������� (����������) ������� � ����������� (iterable) ��� ���������� (����������) �� ���� � ����� ����������.

���� ��� ������ ���� ����������� ��������, �� �� ������ ���� �����������. 
� ���� ������ ������� ���������� ���������� (����������) ������� �� ������� ������������. 
���� ���� ��� ��� ����� ����������� ���������, �� ��������� ����� ���������� (����������) �� ������ ����������.

�������������� �������� �������� key ���������� ������� ������ ���������, ������� ������������ ��� ���������� ����� ��� 
��������� �� ������� �������� ������� (��� �������, key=str.lower).
���� ������ �������� ��������� ������������ (�����������) ��������, �� ������� ���������� ������ �� ������� � �������.

-- Python ������������ (���������� �������)

����: ���� ����������� ��������, ��� ����������� ��� ��� ��� ����� ����������� ����������. �������������� �������� ��������, ��� �������.

�����: ���������� ������� ��� "max" ������� � ���������� ��� "min" �������.

�����������: ��� ����� ���������, �������� �������� ������� � �� ������ ��������� ����������. */

def sortMin(x, y, key):
    if ( key != None and key(x) < key(y) ) or ( key == None and x < y): 
        return x
    return y
    
def sortMax(x, y, key):
    if sortMin(x, y, key) == y :
        return x
    return y
    
def min(*args, key = None):
#    if len(args)==1: args=list(args[0])
    if len(args) == 1: 
        args=list(args[0])
    result = args[0]
    for x in range( 1,len(args) ):
        result = sortMin(result,args[x],key)
    return result

def max(*args, key = None):
    if len(args) == 1: 
        args=list(args[0])
    result = args[0]
    for x in range( 1,len(args) ):
        result = sortMax(result,args[x],key)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")