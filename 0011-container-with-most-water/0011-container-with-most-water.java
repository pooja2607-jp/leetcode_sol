class Solution {
    public int maxArea(int[] height) {
        int maxArea=0;
        int l=0;
        int r=height.length-1;
       while(l<r){
        int currArea=Math.min(height[l],height[r])*(r-l);
        maxArea=Math.max(maxArea,currArea);
        if(height[l]<height[r]){
            l++;
        }else{
            r--;
        }
       }
       return maxArea;
    }
}