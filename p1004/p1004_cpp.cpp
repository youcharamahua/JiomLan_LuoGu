#include<bits/stdc++.h>
using namespace std;

int f[12][12][12][12];
int a[12][12];
int n,x,y,z;
int main() {
    cin>>n>>x>>y>>z;
    while(x!=0||y!=0||z!=0){//输入
        a[x][y]=z;
        cin>>x>>y>>z;
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            for(int k=1;k<=n;k++){
                for(int l=1;l<=n;l++){
                	//因为只能走右或下，所以上一步只有2种结果，与另一条一共4种结果
                	int MAX = 0;
                	MAX = max(f[i-1][j][k-1][l],f[i-1][j][k][l-1]);
                	MAX = max(MAX,max(f[i][j-1][k-1][l],f[i][j-1][k][l-1]));
                    f[i][j][k][l]=MAX+a[i][j]+a[k][l];
                    if(i==k&&l==j){//点只能取走一次
						f[i][j][k][l]-=a[i][j];
					}
                }
            }
        }
    }
    
    cout<<f[n][n][n][n];
    return 0;
}