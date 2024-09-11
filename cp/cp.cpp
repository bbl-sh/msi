#include<bits/stdc++.h> 
using namespace std; 

void solve(){
	int x, ch = 0;
	cin >> x;
	vector<int> ans;
	for (int i = 0; i < x; ++i)
	{
		cin >> ch;
		ans.push_back(ch);
	}
	for (int i = 0,ch = 0, j = x - 1; i < x; ++i)
	{
		if (i % 2 == 0){
			cout << ans[ch] << " ";
			ch++;
		}
		else{
//			continue;
			cout << ans[j] << " ";
			j--;
		}
	}
} 

int main() 
{ 
ios_base::sync_with_stdio(false);cin.tie(NULL); 

#ifndef ONLINE_JUDGE 
freopen("input.txt", "r", stdin);  
freopen("output.txt", "w", stdout); 
#endif 
 
int t;
cin >> t;

while(t--) 
{ 
	solve(); 
	cout<<"\n"; 
} 

return 0; 
} 
