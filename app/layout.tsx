import type React from "react"
import type { Metadata } from "next"
import { Montserrat, Open_Sans, JetBrains_Mono } from "next/font/google"
import "./globals.css"

const montserrat = Montserrat({
  subsets: ["latin"],
  variable: "--font-montserrat",
  display: "swap",
})

const openSans = Open_Sans({
  subsets: ["latin"],
  variable: "--font-open-sans",
  display: "swap",
})

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-jetbrains-mono",
  display: "swap",
})

export const metadata: Metadata = {
  title: "Ranjit Saroj - Cybersecurity Professional",
  description:
    "Experienced cybersecurity specialist specializing in SOC operations, vulnerability assessment, and security tool development.",
  keywords: "cybersecurity, penetration testing, security operations, vulnerability assessment, SOC, VAPT",
    generator: 'v0.app'
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={`${montserrat.variable} ${openSans.variable} ${jetbrainsMono.variable}`}>
      <body className="antialiased">{children}</body>
    </html>
  )
}
