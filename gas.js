function calculateGasFee(gasLimit, baseFee, priorityFee) {
    const gasFee = gasLimit * (baseFee + priorityFee);
    return gasFee;
}


const gasLimit = 21000;
const baseFee = 30;
const priorityFee = 5;

const totalGasFee = calculateGasFee(gasLimit, baseFee, priorityFee);
console.log("Total Gas Fee:", totalGasFee);
