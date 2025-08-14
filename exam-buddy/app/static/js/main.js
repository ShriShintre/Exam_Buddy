// Main JavaScript functionality for Exam Buddy
document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });

    // Study reminder notifications
    function showStudyReminder() {
        if (Notification.permission === 'granted') {
            new Notification('Study Reminder', {
                body: 'Time to get back to studying! 📚',
                icon: '/static/favicon.ico'
            });
        }
    }

    // Request notification permission and set up reminders
    if ('Notification' in window && Notification.permission === 'default') {
        Notification.requestPermission();
    }

    // Set up study reminders every 30 minutes
    if (Notification.permission === 'granted') {
        setInterval(showStudyReminder, 30 * 60 * 1000);
    }

    // Progress bar animation
    const progressBars = document.querySelectorAll('.progress-fill');
    progressBars.forEach(function(bar) {
        const width = bar.style.width;
        bar.style.width = '0%';
        setTimeout(function() {
            bar.style.width = width;
            bar.style.transition = 'width 1s ease-in-out';
        }, 500);
    });
});

// User menu toggle function
function toggleUserMenu() {
    const dropdown = document.getElementById('userDropdown');
    dropdown.classList.toggle('active');
}

// Close user menu when clicking outside
document.addEventListener('click', function(event) {
    const userMenu = document.querySelector('.user-menu');
    const dropdown = document.getElementById('userDropdown');
    
    if (userMenu && dropdown && !userMenu.contains(event.target)) {
        dropdown.classList.remove('active');
    }
});
