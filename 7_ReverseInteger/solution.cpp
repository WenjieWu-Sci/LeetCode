#include <iostream>

class Solution {
public:
    int reverse(int x) {
        int rev= 0;
        while (x!=0) {
            int pop= x%10;
            x/= 10;
            if (rev>INT_MAX/10 || (rev==INT_MAX/10 && pop>7)) return 0;
            if (rev<INT_MIN/10 || (rev==INT_MIN/10 && pop<-8)) return 0;
            rev= rev*10+pop;
        }
        return rev;
    }
};

int main(int argc, char** argv) {
    int org_num= 1234;
    if (argc>1) org_num= atoi(argv[1]);
    Solution rev;
    int rev_num= rev.reverse(org_num);
    std::cout<<org_num<<"<--->"<<rev_num<<std::endl;
    return 0;
}
