import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "临床研究 SAP 生成",
  description: "基于 Protocol 与 CRF 生成统计分析计划（SAP）",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
