import Header from "@/components/Header"
import HeroSection from "@/components/HeroSection"
import StatsSection from "@/components/StatsSection"
import ExpertiseSection from "@/components/ExpertiseSection"
import TerminalSection from "@/components/TerminalSection"
import ExperienceSection from "@/components/ExperienceSection"
import ProjectsSection from "@/components/ProjectsSection"
import SkillsSection from "@/components/SkillsSection"
import ContactSection from "@/components/ContactSection"
import Footer from "@/components/Footer"

export default function Home() {
  return (
    <main className="min-h-screen bg-background">
      <Header />
      <HeroSection />
      <StatsSection />
      <ExpertiseSection />
      <TerminalSection />
      <ExperienceSection />
      <ProjectsSection />
      <SkillsSection />
      <ContactSection />
      <Footer />
    </main>
  )
}
