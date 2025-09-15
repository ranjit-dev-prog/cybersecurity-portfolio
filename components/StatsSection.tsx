"use client"

import { useEffect, useState } from "react"
import { Shield, Target, Wrench, TrendingUp } from "lucide-react"

const stats = [
  { number: "1+", label: "Years Experience", icon: Shield },
  { number: "10+", label: "Security Assessments", icon: Target },
  { number: "15+", label: "Tools Developed", icon: Wrench },
  { number: "100%", label: "Success Rate", icon: TrendingUp },
]

export default function StatsSection() {
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

    const element = document.getElementById("stats-section")
    if (element) observer.observe(element)

    return () => observer.disconnect()
  }, [])

  return (
    <section id="stats-section" className="py-20 bg-secondary/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {stats.map((stat, index) => {
            const Icon = stat.icon
            return (
              <div
                key={stat.label}
                className={`glass rounded-2xl p-8 text-center hover:shadow-xl transition-all duration-500 hover:-translate-y-2 ${
                  isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
                }`}
                style={{ transitionDelay: `${index * 100}ms` }}
              >
                <div className="relative">
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-primary to-accent rounded-t-2xl"></div>
                  <div className="text-accent mb-4 flex justify-center">
                    <Icon size={32} />
                  </div>
                  <div className="text-4xl font-black font-montserrat text-primary mb-2">{stat.number}</div>
                  <div className="text-muted-foreground font-semibold uppercase tracking-wide text-sm">
                    {stat.label}
                  </div>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </section>
  )
}
