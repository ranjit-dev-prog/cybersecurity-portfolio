"use client"

import { useEffect, useState } from "react"

const terminalLines = [
  {
    prompt: "ranjit@cyberlab:~$",
    command: "whoami",
    output: "Cybersecurity Specialist - SOC Operations & VAPT Expert",
  },
  {
    prompt: "ranjit@cyberlab:~$",
    command: "cat /etc/skills.conf",
    output: "Python | Penetration Testing | Security Automation | Threat Analysis",
  },
  {
    prompt: "ranjit@cyberlab:~$",
    command: "ls /projects/",
    output: "security-automation-suite/  threat-detection-system/  cloud-security-tools/",
  },
  {
    prompt: "ranjit@cyberlab:~$",
    command: "systemctl status threat-monitoring",
    output: "● threat-monitoring.service - Active and monitoring cyber threats 24/7",
  },
  {
    prompt: "ranjit@cyberlab:~$",
    command: "nmap -sC -sV target.com",
    output: "Starting Nmap scan... Vulnerability assessment in progress...",
  },
]

export default function TerminalSection() {
  const [visibleLines, setVisibleLines] = useState(0)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          const interval = setInterval(() => {
            setVisibleLines((prev) => {
              if (prev >= terminalLines.length) {
                clearInterval(interval)
                return prev
              }
              return prev + 1
            })
          }, 800)
        }
      },
      { threshold: 0.3 },
    )

    const element = document.getElementById("terminal-section")
    if (element) observer.observe(element)

    return () => observer.disconnect()
  }, [])

  return (
    <section id="terminal-section" className="py-20 bg-secondary/20">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="glass rounded-3xl overflow-hidden shadow-2xl">
          {/* Terminal Header */}
          <div className="bg-muted/50 px-6 py-4 flex items-center gap-3 border-b border-border">
            <div className="flex gap-2">
              <div className="w-3 h-3 rounded-full bg-red-500"></div>
              <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
              <div className="w-3 h-3 rounded-full bg-green-500"></div>
            </div>
            <span className="text-muted-foreground font-mono text-sm ml-4">security-operations@cyberlab</span>
          </div>

          {/* Terminal Body */}
          <div className="bg-slate-900 p-6 font-mono text-sm min-h-[400px]">
            {terminalLines.slice(0, visibleLines).map((line, index) => (
              <div key={index} className="mb-4 animate-slide-up">
                <div className="flex items-center">
                  <span className="text-cyan-400 font-semibold">{line.prompt}</span>
                  <span className="text-purple-400 ml-2 font-medium">{line.command}</span>
                </div>
                <div className="text-gray-300 ml-6 mt-1 opacity-90">{line.output}</div>
              </div>
            ))}
            {visibleLines < terminalLines.length && (
              <div className="flex items-center">
                <span className="text-cyan-400 font-semibold">ranjit@cyberlab:~$</span>
                <span className="ml-2 w-2 h-5 bg-white animate-pulse"></span>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  )
}
