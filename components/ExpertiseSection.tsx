"use client"

import { useEffect, useState } from "react"
import { Shield, Search, Settings } from "lucide-react"

const expertise = [
  {
    icon: Shield,
    title: "Security Operations Center (SOC)",
    description:
      "Comprehensive security monitoring, incident response, and threat analysis with expertise in SIEM platforms and security orchestration.",
    skills: [
      "Security Monitoring",
      "Incident Response & Analysis",
      "SIEM Implementation & Management",
      "Threat Intelligence Analysis",
      "Security Automation & Orchestration",
    ],
  },
  {
    icon: Search,
    title: "Vulnerability Assessment & Penetration Testing",
    description:
      "Systematic evaluation of security weaknesses across applications, networks, and infrastructure with detailed remediation guidance.",
    skills: [
      "Web Application Security Testing",
      "Network Infrastructure Assessment",
      "Cloud Security Evaluation",
      "Compliance Security Auditing",
      "Risk Assessment & Management",
    ],
  },
  {
    icon: Settings,
    title: "Security Tool Development",
    description:
      "Custom security solutions and automation frameworks designed to enhance organizational security posture and operational efficiency.",
    skills: [
      "Python Security Automation",
      "Custom Security Tools",
      "API Security Testing",
      "Automated Scanning Frameworks",
      "Security Reporting Solutions",
    ],
  },
]

export default function ExpertiseSection() {
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

    const element = document.getElementById("expertise")
    if (element) observer.observe(element)

    return () => observer.disconnect()
  }, [])

  return (
    <section id="expertise" className="py-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-black font-montserrat text-primary mb-6">Core Expertise</h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Comprehensive cybersecurity capabilities across security operations, assessment, and tool development
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {expertise.map((item, index) => {
            const Icon = item.icon
            return (
              <div
                key={item.title}
                className={`glass rounded-3xl p-8 hover:shadow-2xl transition-all duration-500 hover:-translate-y-4 group ${
                  isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
                }`}
                style={{ transitionDelay: `${index * 200}ms` }}
              >
                <div className="flex items-center gap-4 mb-6">
                  <div className="w-16 h-16 bg-gradient-to-br from-primary to-accent rounded-2xl flex items-center justify-center text-white shadow-lg group-hover:shadow-xl transition-shadow duration-300">
                    <Icon size={32} />
                  </div>
                  <h3 className="text-xl font-bold font-montserrat text-foreground">{item.title}</h3>
                </div>

                <p className="text-muted-foreground mb-6 leading-relaxed">{item.description}</p>

                <ul className="space-y-3">
                  {item.skills.map((skill) => (
                    <li key={skill} className="flex items-center text-foreground">
                      <span className="text-accent mr-3">⚡</span>
                      {skill}
                    </li>
                  ))}
                </ul>
              </div>
            )
          })}
        </div>
      </div>
    </section>
  )
}
