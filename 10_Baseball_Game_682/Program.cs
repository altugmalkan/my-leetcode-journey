
public class Solution
{
    public static int BaseballGame(string[] ops)
    {
        List<int> myList = new List<int>();

        for (int i = 0; i < ops.Length; i++)
        {
            if (ops[i] == "C")
            {
                myList.RemoveAt(myList.Count - 1);
            }
            else if (ops[i] == "D")
            {
                myList.Add(myList[myList.Count - 1] * 2);
            }
            else if (ops[i] == "+")
            {
                myList.Add(myList[myList.Count - 1] + myList[myList.Count - 2]);
            }
            else
            {
                myList.Add(int.Parse(ops[i]));
            }
        }

        int sum = 0;
        for (int i = 0; i < myList.Count; i++)
        {
            sum += myList[i];
        }
        return sum;
    }

    public static void Main()
    {
        string[] ops = new string[] { "5", "2", "C", "D", "+" };
        string[] ops2 = new string[] { "5", "-2", "4", "C", "D", "9", "+", "+" };
        string[] ops3 = new string[] { "1", "C" };
        Console.WriteLine(BaseballGame(ops));
        Console.WriteLine(BaseballGame(ops2));
        Console.WriteLine(BaseballGame(ops3));

    }
}