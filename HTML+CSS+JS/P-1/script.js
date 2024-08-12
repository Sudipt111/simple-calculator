document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    
    const petName = params.get('petName');
    const petType = params.get('petType');
    const pedigreed = params.get('pedigreed') === 'true' ? 'Yes' : 'No';
    
    const summaryDiv = document.getElementById('summary');
    
    const summaryContent = `
        <p><strong>Pet Name:</strong> ${petName}</p>
        <p><strong>Pet Type:</strong> ${petType}</p>
        <p><strong>Pedigreed:</strong> ${pedigreed}</p>
    `;
    
    summaryDiv.innerHTML = summaryContent;
});
