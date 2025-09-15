"use client"

import { useEffect, useState } from "react"
import { MapPin, Phone, Mail, Linkedin, Github } from "lucide-react"

const contactInfo = [
  { icon: MapPin, title: "Location", value: "Mumbai, India", href: null },
  { icon: Phone, title: "Phone", value: "+91 9867470618", href: "tel:+91 9867470618" },
  { icon: Mail, title: "Email", value: "ranjitsaroj393@gmail.com", href: "mailto:ranjitsaroj393@gmail.com" },
  {
    icon: Linkedin,
    title: "LinkedIn",
    value: "View Profile",
    href: "https://www.linkedin.com/in/ranjit-saroj-593786244/",
  },
  { icon: Github, title: "GitHub", value: "View Repositories", href: "https://github.com/ranjit-dev-prog" },
]

export default function ContactSection() {
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

    const element = document.getElementById("contact")
    if (element) observer.observe(element)

    return () => observer.disconnect()
  }, [])

  return (
    <section id="contact" className="py-20 bg-secondary/20">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-black font-montserrat text-primary mb-6">Get in Touch</h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Let's discuss how I can help strengthen your security posture
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {contactInfo.map((item, index) => {
            const Icon = item.icon
            return (
              <div
                key={index}
                className={`glass rounded-3xl p-8 text-center hover:shadow-2xl transition-all duration-500 hover:-translate-y-4 group cursor-pointer ${
                  isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
                }`}
                style={{ transitionDelay: `${index * 100}ms` }}
              >
                <div className="w-20 h-20 bg-gradient-to-br from-primary to-accent rounded-full flex items-center justify-center mx-auto mb-6 text-white shadow-lg group-hover:shadow-xl transition-shadow duration-300">
                  <Icon size={32} />
                </div>
                <h3 className="text-xl font-bold font-montserrat text-foreground mb-3">{item.title}</h3>
                <p className="text-accent font-semibold hover:text-primary transition-colors duration-300">
                  {item.value}
                </p>
              </div>
            )
          })}
        </div>
      </div>
    </section>
  )
}
