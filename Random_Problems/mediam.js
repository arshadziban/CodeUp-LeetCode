function findMedianSortedArrays(nums1, nums2) {
  if (nums1.length > nums2.length) {
    [nums1, nums2] = [nums2, nums1];
  }

  const m = nums1.length;
  const n = nums2.length;
  let left = 0, right = m;
  const half = Math.floor((m + n + 1) / 2);

  while (left <= right) {
    const i = Math.floor((left + right) / 2);
    const j = half - i;

    const Aleft  = i > 0 ? nums1[i - 1] : -Infinity;
    const Aright = i < m ? nums1[i]     :  Infinity;
    const Bleft  = j > 0 ? nums2[j - 1] : -Infinity;
    const Bright = j < n ? nums2[j]     :  Infinity;

    if (Aleft <= Bright && Bleft <= Aright) {
      if ((m + n) % 2 === 1) {
        return Math.max(Aleft, Bleft);
      }
      return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2;
    } else if (Aleft > Bright) {
      right = i - 1;
    } else {
      left = i + 1;
    }
  }

  throw new Error("Invalid input.");
}

console.log(findMedianSortedArrays([1,3], [2]));    
console.log(findMedianSortedArrays([1,2], [3,4]));  
console.log(findMedianSortedArrays([], [1]));       
console.log(findMedianSortedArrays([0,0], [0,0]));  
