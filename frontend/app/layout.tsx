import type { Metadata } from "next";
import { VideoAnalyzer } from "@/components/video-analyzer";
import "./globals.css";

export const metadata: Metadata = {
  title: "Video Intelligence System",
  description: "AI-powered YouTube video analysis tool",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <VideoAnalyzer />
      </body>
    </html>
  );
}
