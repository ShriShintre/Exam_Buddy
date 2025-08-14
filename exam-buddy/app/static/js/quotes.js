document.addEventListener('DOMContentLoaded', function() {
    // Motivational quotes for studying
    const quotes = [
        { text: "Success is not the key to happiness. Happiness is the key to success.", author: "Albert Schweitzer" },
        { text: "The only way to do great work is to love what you do.", author: "Steve Jobs" },
        { text: "You miss 100% of the shots you don't take.", author: "Wayne Gretzky" },
        { text: "Education is the most powerful weapon which you can use to change the world.", author: "Nelson Mandela" },
        { text: "The future belongs to those who believe in the beauty of their dreams.", author: "Eleanor Roosevelt" },
        { text: "It is during our darkest moments that we must focus to see the light.", author: "Aristotle" },
        { text: "Success is not final, failure is not fatal: it is the courage to continue that counts.", author: "Winston Churchill" },
        { text: "The way to get started is to quit talking and begin doing.", author: "Walt Disney" },
        { text: "Don't let yesterday take up too much of today.", author: "Will Rogers" },
        { text: "You learn more from failure than from success.", author: "Unknown" },
        { text: "If you are working on something exciting, you don't have to be pushed.", author: "Steve Jobs" },
        { text: "Success is walking from failure to failure with no loss of enthusiasm.", author: "Winston Churchill" }
    ];

    const quoteText = document.getElementById('quote-text');
    const quoteAuthor = document.getElementById('quote-author');

    function displayRandomQuote() {
        const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
        quoteText.textContent = `"${randomQuote.text}"`;
        quoteAuthor.textContent = `- ${randomQuote.author}`;
    }

    setInterval(displayRandomQuote, 10000); // Change quote every 10 seconds
    displayRandomQuote(); // Initial display
});
