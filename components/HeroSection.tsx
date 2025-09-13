"use client"

import { useEffect, useState } from "react"
import { Shield, Lock, Zap } from "lucide-react"
import { Button } from "@/components/ui/button"

export default function HeroSection() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    setIsVisible(true)
  }, [])

  return (
    <section
      id="home"
      className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-background via-secondary to-background"
    >
      {/* Floating Elements */}
      <div className="absolute inset-0 pointer-events-none">
        <div className="absolute top-20 left-10 text-primary/30 animate-float">
          <Shield size={48} />
        </div>
        <div className="absolute top-60 right-20 text-accent/30 animate-float" style={{ animationDelay: "2s" }}>
          <Lock size={36} />
        </div>
        <div className="absolute bottom-40 left-20 text-primary/30 animate-float" style={{ animationDelay: "4s" }}>
          <Zap size={42} />
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        {/* Status Badge */}
        <div
          className={`inline-block glass rounded-full px-6 py-3 mb-8 transition-all duration-1000 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
          }`}
        >
          <span className="text-accent font-semibold">Your trusted cybersecurity partner</span>
        </div>

        {/* Main Title */}
        <h1
          className={`text-5xl md:text-7xl font-black font-montserrat mb-6 transition-all duration-1000 delay-200 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
          }`}
        >
          Safeguarding
          <br />
          your digital <span className="text-primary">world</span>
        </h1>

        {/* Subtitle */}
        <p
          className={`text-xl md:text-2xl text-accent font-semibold mb-6 transition-all duration-1000 delay-400 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
          }`}
        >
          SOC Operations | Vulnerability Assessment | Security Architecture
        </p>

        {/* Description */}
        <p
          className={`text-lg text-muted-foreground max-w-4xl mx-auto mb-12 leading-relaxed transition-all duration-1000 delay-600 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
          }`}
        >
          We provide advanced security solutions to safeguard your business from cyber threats. Experienced
          cybersecurity professional specializing in security operations, vulnerability assessment, and custom security
          tool development.
        </p>

        {/* CTA Buttons */}
        <div
          className={`flex flex-col sm:flex-row gap-4 justify-center transition-all duration-1000 delay-800 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"
          }`}
        >
          <Button
            size="lg"
            className="bg-primary hover:bg-primary/90 text-primary-foreground px-8 py-4 text-lg font-semibold rounded-full shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
          >
            Get a free consultation
          </Button>
          <Button
            variant="outline"
            size="lg"
            className="glass border-primary/30 hover:border-primary text-foreground hover:text-primary px-8 py-4 text-lg font-semibold rounded-full transition-all duration-300 hover:-translate-y-1 bg-transparent"
          >
            View Portfolio
          </Button>
        </div>
      </div>
    </section>
  )
}
