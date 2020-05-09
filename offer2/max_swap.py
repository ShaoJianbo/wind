class Solution:
    def maximumSwap(self, num: int) -> int:
        """考虑最大交换价值"""
        num_str = str(num)
        cur_pos = swap_pos = 0

        for i, n in enumerate(str(num_str)):
            cur_n = int(n)
            cur_pos = swap_pos = i
            next_arr = [int(_) for _ in num_str[i + 1:]]
            if next_arr:
                max_n = max(next_arr)
            else:
                break
            print(f"{cur_pos}-->{cur_n}-->{max_n}")
            if cur_pos != swap_pos:
                break
            if cur_n >= max_n:
                continue
            else:
                for j, n1 in enumerate(str(num_str[i+1:])):
                    if int(n1) == max_n:
                        print(f"j=>{j}")
                        swap_pos = j + cur_pos+1
            print(f"{cur_pos}-->{swap_pos}")
            if swap_pos != cur_pos:
                break
        if swap_pos != cur_pos:
            num_arr = [i for i in num_str]
            num_arr[swap_pos], num_arr[cur_pos] = num_arr[cur_pos], num_arr[
                swap_pos]
            return int(''.join(num_arr))
        else:
            return num


if __name__ == '__main__':
    so = Solution()
    num = 2736
    # num = 9973
    # num = 98368
    # num = 1993
    res = so.maximumSwap(num)
    print(f"{res}")
