class Program
{
    public static int MajorityElement(int[] nums)
    {
        Dictionary<int, int> dict = new Dictionary<int, int>();

        foreach (var num in nums)
        {
            if (dict.ContainsKey(num))
            {
                dict[num] += 1;
            }
            else
            {
                dict[num] = 1;
            }
        }

        int maxCount = 0;
        int res = nums[0];

        foreach (var pair in dict)
        {
            if (pair.Value > maxCount)
            {
                maxCount = pair.Value;
                res = pair.Key;
            }
        }
        return res;
    }

    public static int MajorityElement2(int[] nums)
    {
        int count = 0;
        int value = 0;

        foreach (var num in nums)
        {
            if (count == 0)
            {
                value = num;
                count = 1;
            }
            else if (num == value)
            {
                count++;
            }
            else
            {
                count--;
            }
        }
        return value;
    }

    public static void Main()
    {
        int[] nums = new int[] { 2, 2, 3, 3, 3, 3, 2 };

        int result = MajorityElement2(nums);

        Console.WriteLine(result);
    }
    

}