string Solution::solve(vector<int> &A) {
  long long ans = 0;
  int l = A.size();
  for (int i = 0; i < l; i++){
    ans += (long long) A[i];
  }
  return to_string(ans);
}
