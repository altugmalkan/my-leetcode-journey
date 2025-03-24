using System;
using System.Collections.Generic;

public class Solution 
{

    public static void ReverseString(char[] s)
    {
        int l = 0;
        int r = s.Length - 1;

        while (l < r)
        {
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l++;
            r--;
        }
    }

    public static void ReverseString2(char [] s)
    {
        Stack<char> stack = new Stack<char>();
        foreach(char c in s)
        {
            stack.Push(c);
        }
        for(int i=0; i<s.Length; i++)
        {
            s[i] = stack.Pop();
        }

    }

    public static void Main()
    {
        char[] s = new char[] { 'h', 'e', 'l', 'l', 'o' };
        Console.WriteLine(s);
        ReverseString2(s);
        Console.WriteLine(s);
    }
}

