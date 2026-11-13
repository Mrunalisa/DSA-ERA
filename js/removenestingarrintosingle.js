let arr = [1, 2, [3], 4, 5, 6];

for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
        for (let j = 0; j < arr[i].length; j++) {
            console.log(arr[i][j]);
        }
    } else {
        console.log(arr[i]);
    }
}