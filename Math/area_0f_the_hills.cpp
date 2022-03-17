string Solution::solve(vector<int> &A) {
    string output;
    int l = A.size();
	if (l == 1){
        output = to_string(A[0]);
        return output; 
    }
    else{
        float starting_area = A[0]/2.0;
        float ending_area = A[l-1]/2.0;
        float intermediate_area = 0.0;
        for (int i = 0; i < l-1; i++){
        float trapezium_area = float(A[i] + A[i+1])/(2.0);
        intermediate_area = intermediate_area + trapezium_area;
        }
        float total_area = starting_area + ending_area + intermediate_area;
        int total_area_int = int(total_area);
        output = to_string(total_area_int);
        return output; 
    }
}
