class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = [1]
        right_product = [1]

        for num in nums[:-1]:
            left_product.append(num * left_product[-1])

        for num in nums[::-1][:-1]:
            right_product.append(num * right_product[-1])

        right_product = right_product[::-1]
        product_except_self = []
        for i in range(len(nums)):
            product_except_self.append(left_product[i] * right_product[i])
        
        return product_except_self
