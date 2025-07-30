import React, { useState } from 'react'

export default function ChatBox() {
  const [query, setQuery] = useState("")
  const [response, setResponse] = useState("")
  const [loading, setLoading] = useState(false)

  const handleSend = async () => {
    if (!query.trim()) return
    setLoading(true)
    try {
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
      })

      const data = await res.json()
      setResponse(data.response || "No response received.")
    } catch (error) {
      setResponse("❌ Error connecting to server.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-2xl mx-auto mt-10 p-6 bg-white rounded-xl shadow-lg space-y-6 border border-gray-200">
      <h1 className="text-3xl font-bold text-center text-blue-600">💬 AI Chat Assistant</h1>

      <textarea
        className="w-full h-28 p-4 border border-gray-300 rounded-md resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
        placeholder="Type your question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button
        onClick={handleSend}
        disabled={loading}
        className={`w-full py-3 text-white font-semibold rounded-md transition-all duration-200 ${
          loading ? "bg-gray-400 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
        }`}
      >
        {loading ? "Thinking..." : "Ask"}
      </button>

      {response && (
        <div className="p-4 bg-gray-100 border border-gray-300 rounded-md">
          <h2 className="font-semibold text-gray-700 mb-2">Answer:</h2>
          <p className="text-gray-800 whitespace-pre-line">{response}</p>
        </div>
      )}
    </div>
  )
}
