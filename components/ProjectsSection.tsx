"use client"

import { useEffect, useState } from "react"
import { Code, Shield, Cloud } from "lucide-react"

const projects = [
  {
    icon: Code,
    title: "Security Automation Framework",
    description: "Comprehensive Python-based toolkit for automated security testing and vulnerability assessment.",
    features: [
      "Automated port scanning and service detection",
      "Directory enumeration with intelligent wordlists",
      "Subdomain discovery and DNS analysis",
      "SSL/TLS certificate validation",
      "Comprehensive security reporting",
    ],
  },
  {
    icon: Shield,
    title: "Threat Detection System",
    description: "Advanced monitoring solution for proactive threat identification and incident response.",
    features: [
      "Real-time log analysis and correlation",
      "Behavioral anomaly detection",
      "Automated alert prioritization",
      "Integration with existing security tools",
      "Executive dashboard and reporting",
    ],
  },
  {
    icon: Cloud,
    title: "Cloud Security Assessment Tool",
    description: "Specialized framework for evaluating cloud infrastructure security and compliance.",
    features: [
      "Multi-cloud environment scanning",
      "IAM configuration analysis",
      "Resource security evaluation",
      "Compliance framework mapping",
      "Automated remediation guidance",
    ],
  },
]

export default function ProjectsSection() {
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

    const element = document.getElementById("projects")
    if (element) observer.observe(element)

    return () => observer.disconnect()
  }, [])

  return (
    <section id="projects" className="py-20 bg-secondary/20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-black font-montserrat text-primary mb-6">Highlighted Projects</h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Key security tools and solutions designed and implemented for real-world challenges
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {projects.map((project, index) => {
            const Icon = project.icon
            return (
              <div
                key={project.title}
                className={`glass rounded-3xl p-8 hover:shadow-2xl transition-all duration-500 hover:-translate-y-4 group ${
                  isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
                }`}
                style={{ transitionDelay: `${index * 200}ms` }}
              >
                <div className="flex items-center gap-4 mb-6">
                  <div className="w-16 h-16 bg-gradient-to-br from-primary to-accent rounded-2xl flex items-center justify-center text-white shadow-lg group-hover:shadow-xl transition-shadow duration-300">
                    <Icon size={32} />
                  </div>
                  <h3 className="text-xl font-bold font-montserrat text-foreground">{project.title}</h3>
                </div>

                <p className="text-muted-foreground mb-6 leading-relaxed">{project.description}</p>

                <ul className="space-y-3">
                  {project.features.map((feature) => (
                    <li key={feature} className="flex items-start text-foreground">
                      <span className="text-accent mr-3 mt-1">⚡</span>
                      <span className="text-sm leading-relaxed">{feature}</span>
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
