import sys

class BinaryTreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def size(self):
        return len(self.queue)

    # popping least frequent item
    def delete(self):
        min_index = 0
        try:
            for i in range(len(self.queue)):
                if self.queue[i].freq < self.queue[min_index].freq:
                    min_index = i

            item = self.queue[min_index]
            del self.queue[min_index]
            return item
        except IndexError:
            print()
            exit()


def huffman_encoding(data):
    if not data:
        return None, None

    frequency_dict = {}
    for c in data:
        frequency_dict[c] = frequency_dict.get(c, 0) + 1

    PQ = PriorityQueue()
    for k, v in frequency_dict.items():
        new_obj = BinaryTreeNode(k, v)
        PQ.insert(new_obj)

    while PQ.size() > 1:
        min_el = PQ.delete()
        max_el = PQ.delete()
        sum_freq = min_el.freq + max_el.freq
        new_node = BinaryTreeNode(None, sum_freq)
        new_node.left = min_el
        new_node.right = max_el
        PQ.insert(new_node)
        root = new_node

    # generate unique binary code for each character
    binary_codes = generate_binary_codes(root)

    # generate encoded data
    encoded_data = ""
    for c in data:
        encoded_data += binary_codes[c]
    return encoded_data, root


def generate_binary_codes(tree):
    binary_cods = dict()

    def traverse(tree, s):
        if tree.char is not None:
            binary_cods[tree.char] = s
            return
        traverse(tree.left, s + '0')
        traverse(tree.right, s + '1')

    traverse(tree, '')
    return binary_cods


def huffman_decoding(data, tree):
    root = tree
    decoded_data = ""

    i = 0
    while i < len(data):
        while root.char is None:
            if data[i] == '0':
                root = root.left
                i += 1
            elif data[i] == '1':
                root = root.right
                i += 1
        decoded_data += root.char
        root = tree

    return decoded_data


# testcase1
a_great_sentence = "The bird is the word"


'''
NOTE: sys.getsizeof():
Return the size of an object in bytes. The object can be any type of object. All built-in objects will return correct results, 
but this does not have to hold true for third-party extensions as it is implementation specific.
'''

print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))
print("The string size of encoded data is {}".format(len(encoded_data)))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))


# testcase2: longer sentence

a_great_sentence = "Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph."


print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))
print("The string size of encoded data is {}".format(len(encoded_data)))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))


# Testcase3: Longer text

f = open("long_text", "r")
a_great_sentence = f.read()

print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))
print("The string size of encoded data is {}".format(len(encoded_data)))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
