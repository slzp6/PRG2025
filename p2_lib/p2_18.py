""" p2_18.py """


class MyStack:
    """My stack."""

    def __init__(self):
        self.data = []

    def push(self, data):
        """Push."""
        self.data.append(data)

    def pop(self):
        """Pop."""
        return self.data.pop()

    def display(self):
        """Display."""
        print(self.data)


st = MyStack()

st.display()
st.push('A')
st.push('B')
st.push('C')
st.display()

print(" pop:", st.pop())
print(" pop:", st.pop())
print(" pop:", st.pop())
st.display()
