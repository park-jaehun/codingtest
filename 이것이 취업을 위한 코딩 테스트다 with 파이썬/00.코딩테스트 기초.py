# N, M, K�� ������ �������� �����Ͽ� �Է¹ޱ�
n,m,k = map(int, input().split())
data = map(int, input().split())

data.sort() # �Է¹��� �� ����
first = data[n - 1] # ���� ū ��
second = data[n - 2] # �� ��°�� ū ��

# ���� ū ���� �������� Ƚ�� ���
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # ���� ū �� ���ϱ�
result += (m - count ) * second # �� ��°�� ū �� ���ϱ�

print(result)
