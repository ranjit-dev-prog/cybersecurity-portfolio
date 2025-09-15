"use client"

import { useEffect, useState } from "react"
import { Code, Shield, Cloud, Award } from "lucide-react"

const skillCategories = [
  {
    title: "Technical Skills",
    icon: Code,
    skills: ["Python", "Bash", "PowerShell", "JavaScript", "SQL", "Linux/Unix", "Windows Server", "VMware", "Docker"],
  },
  {
    title: "Security Tools",
    icon: Shield,
    skills: [
      "Burp Suite",
      "Nmap",
      "Metasploit",
      "Wireshark",
      "Nessus",
      "OWASP ZAP",
      "OpenVAS",
      "Nuclei",
      "SQLMap",
      "Gobuster",
    ],
  },
  {
    title: "Platforms & Cloud",
    icon: Cloud,
    skills: ["AWS", "Azure", "Google Cloud", "Splunk", "ELK Stack", "QRadar", "Sentinel", "CrowdStrike", "Rapid7"],
  },
  {
    title: "Certifications",
    icon: Award,
    skills: ["EC-Council cybersecurity in business","cisco networking basics"],
  },
]

export default function SkillsSection() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true)
        }
      },
      { threshold: 0.1 },
    )

    const element = document.getElementById("skills")
    if (element) observer.observe(element)

    return () => observer.disconnect()
  }, [])

  return (
    <section id="skills" className="py-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-black font-montserrat text-primary mb-6">Technical Arsenal</h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Core competencies in security tools, platforms, and cybersecurity certifications
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {skillCategories.map((category, index) => {
            const Icon = category.icon
            return (
              <div
                key={category.title}
                className={`glass rounded-3xl p-8 hover:shadow-xl transition-all duration-500 hover:-translate-y-2 ${
                  isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
                }`}
                style={{ transitionDelay: `${index * 150}ms` }}
              >
                <div className="flex items-center gap-3 mb-6">
                  <Icon className="text-accent" size={24} />
                  <h3 className="text-xl font-bold font-montserrat text-foreground">{category.title}</h3>
                </div>

                <div className="flex flex-wrap gap-3">
                  {category.skills.map((skill, skillIndex) => (
                    <span
                      key={skill}
                      className={`bg-gradient-to-r from-primary to-accent text-white px-4 py-2 rounded-full text-sm font-semibold hover:shadow-lg hover:-translate-y-1 transition-all duration-300 cursor-default ${
                        isVisible ? "opacity-100 scale-100" : "opacity-0 scale-95"
                      }`}
                      style={{ transitionDelay: `${index * 150 + skillIndex * 50}ms` }}
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </section>
  )
}
