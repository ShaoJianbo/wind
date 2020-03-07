class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = self.rm_zero(version1)
        version2 = self.rm_zero(version2)
        print(version1, "-->", version2)
        return self.cmp_version(version1, version2)

    def rm_zero(self, version):
        version_arr = version.split(".")
        version = "1"
        for v in version_arr:
            while len(v) > 1 and v.startswith("0"):
                v = v[1:]
            version = version + "." + v
        # 转换成整数

        return version[2:]

    def cmp_version(self, v1, v2):
        v1_arr = v1.split(".")
        v2_arr = v2.split(".")
        print(v1_arr,"-->", v2_arr)
        v1_num = sum([int(n)*10**(5-i) for i,n in enumerate(v1_arr)])
        v2_num = sum([int(n)*10**(5-i) for i,n in enumerate(v2_arr)])
        print(v1_num, "-->", v2_num)
        if v1_num == v2_num:
            return 0
        elif v1_num > v2_num:
            return 1
        else:
            return -1

if __name__ == '__main__':
    so = Solution()
    version1 = "1.01"
    version2 = "1.001"
    version1, version2 = ["1.2", "1.10"]
    res = so.compareVersion(version1, version2)
    print(res)
