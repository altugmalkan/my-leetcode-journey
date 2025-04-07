class Program
{
    public static int SearchInsert(int[] nums, int target)
    {
        int left = 0;
        int right = nums.Length - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            // int mid = (right +left) / 2; // This can cause overflow
            if (nums[mid] == target)
            {
                return mid;


            else if (target > nums[mid])
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }

            return left;
        }
    }

    /* 
    I wrote binary search to remember how it works
    This is not needed for the solution, 
    How ever you need to know how it works for you to solve the Search Insert problem
    */
    public static int BinarySearch(int[] nums, int target)
    {
        int left = 0;
        int right = nums.Length - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
            {
                return target;
            }
            else if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }

        return -1;
    }

    public static void Main(string[] args)
    {
        int[] nums = { 1, 3, 5, 6 };
        int target = 0;
        int result = SearchInsert(nums, target);
        Console.WriteLine(result);
    }
}