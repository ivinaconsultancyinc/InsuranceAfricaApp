 fetch("http://127.0.0.1:8000/dashboard/metrics")
    .then(response => response.json())
    .then(data => {
        document.getElementById("commissions").textContent = data.total_commissions;
        document.getElementById("payroll").textContent = data.total_payroll;

        const labels = data.trial_balance.map(item => item.account);
        const debitData = data.trial_balance.map(item => item.total_debit);
        const creditData = data.trial_balance.map(item => item.total_credit);

        const ctx = document.getElementById("trialChart").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Debit",
                        data: debitData,
                        backgroundColor: "rgba(75, 192, 192, 0.6)"
                    },
                    {
                        label: "Credit",
                        data: creditData,
                        backgroundColor: "rgba(255, 99, 132, 0.6)"
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Trial Balance Overview'
                    }
                }
            }
        });
    });

