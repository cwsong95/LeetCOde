# Time complexity: O (N)
const anagramMappings1 = (A: number[], B: number[]): number[] => {
	const map = {}   # or map = {}
	let output = []
	
	for(let i = 0; i < B.length; i++) {
		map.set(B[i], i)     # <element, index>
		// Map { 50 => 0, 12 => 1, 32 => 2, 46 => 3, 28 => 4 }
	}

	for(const cv of A) {
		output.push(map.get(cv));
	}

	return output;
}

# Time complexity: O (N^2)
const anagramMappings1 = (A: number[], B: number[]): number[] => {
	let output = [];
	for(let i = 0; i < A.length; i++) {
		output.push(B.indexOf(A[i]));
	}

	return output;
}