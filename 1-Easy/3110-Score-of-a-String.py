# Bạn được cấp một chuỗi s. Điểm của một chuỗi được định nghĩa là tổng của sự khác biệt tuyệt đối giữa các giá trị ASCII của các ký tự liền kề.

# Trả về điểm của . s

 

# Ví dụ 1:

# Đầu vào: s = "xin chào"

# Đầu ra: 13

# Giải trình:

# Giá trị ASCII của các ký tự trong slà: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. Vì vậy, số điểm ssẽ là |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Ví dụ 2:

# Đầu vào: s = "zaz"

# Đầu ra: 50

# Giải trình:

# Giá trị ASCII của các ký tự trong slà: 'z' = 122, 'a' = 97. Vì vậy, số điểm ssẽ là |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

# Hạn chế:

# 2 <= s.length <= 100
# schỉ bao gồm các chữ cái tiếng Anh viết thường.
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))
        return score       