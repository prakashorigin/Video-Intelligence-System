'use client';

import React, { useState } from 'react';
import {
  ChevronDown,
  ChevronUp,
  BookOpen,
  Lightbulb,
  Clock,
  FileText,
  Copy,
  Check,
} from 'lucide-react';

interface VideoResultsProps {
  data: any;
}

export function VideoResults({ data }: VideoResultsProps) {
  const [expandedSections, setExpandedSections] = useState<Record<string, boolean>>({
    metadata: true,
    summary: true,
    keyPoints: true,
    timestampedAnalysis: true,
    captions: false,
  });

  const [copiedIndex, setCopiedIndex] = useState<string | null>(null);

  const toggleSection = (section: string) => {
    setExpandedSections((prev) => ({
      ...prev,
      [section]: !prev[section],
    }));
  };

  const handleCopy = (text: string, index: string) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  const formatTime = (seconds: number): string => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = Math.floor(seconds % 60);

    if (hours > 0) {
      return `${hours}:${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }
    return `${minutes}:${secs.toString().padStart(2, '0')}`;
  };

  const CollapsibleSection = ({
    title,
    icon: Icon,
    section,
    children,
  }: {
    title: string;
    icon: any;
    section: string;
    children: React.ReactNode;
  }) => (
    <div className="mb-4 border border-gray-200 rounded-lg overflow-hidden">
      <button
        onClick={() => toggleSection(section)}
        className="w-full bg-gradient-to-r from-gray-50 to-gray-100 p-4 flex items-center justify-between hover:bg-gray-100 transition"
      >
        <div className="flex items-center gap-3">
          <Icon className="w-5 h-5 text-blue-600" />
          <h3 className="font-semibold text-gray-900">{title}</h3>
        </div>
        {expandedSections[section] ? (
          <ChevronUp className="w-5 h-5 text-gray-600" />
        ) : (
          <ChevronDown className="w-5 h-5 text-gray-600" />
        )}
      </button>
      {expandedSections[section] && (
        <div className="p-4 bg-white border-t border-gray-200">
          {children}
        </div>
      )}
    </div>
  );

  return (
    <div className="space-y-4">
      {/* Metadata */}
      <CollapsibleSection
        title="Video Information"
        icon={FileText}
        section="metadata"
      >
        {data.metadata && (
          <div className="space-y-3">
            <div>
              <label className="text-sm font-medium text-gray-600">Title</label>
              <p className="text-gray-900 font-medium">{data.metadata.title}</p>
            </div>
            <div>
              <label className="text-sm font-medium text-gray-600">Channel</label>
              <p className="text-gray-900">{data.metadata.channel}</p>
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium text-gray-600">Duration</label>
                <p className="text-gray-900">{formatTime(data.metadata.duration)}</p>
              </div>
              <div>
                <label className="text-sm font-medium text-gray-600">Views</label>
                <p className="text-gray-900">
                  {(data.metadata.views || 0).toLocaleString()}
                </p>
              </div>
            </div>
            {data.metadata.upload_date && (
              <div>
                <label className="text-sm font-medium text-gray-600">Upload Date</label>
                <p className="text-gray-900">
                  {new Date(data.metadata.upload_date).toLocaleDateString()}
                </p>
              </div>
            )}
            {data.metadata.description && (
              <div>
                <label className="text-sm font-medium text-gray-600">Description</label>
                <p className="text-gray-900 text-sm line-clamp-3">
                  {data.metadata.description}
                </p>
              </div>
            )}
          </div>
        )}
      </CollapsibleSection>

      {/* Summary */}
      {data.summary && (
        <CollapsibleSection title="Summary" icon={BookOpen} section="summary">
          <div className="space-y-3">
            <p className="text-gray-700 leading-relaxed">{data.summary}</p>
          </div>
        </CollapsibleSection>
      )}

      {/* Key Points */}
      {data.key_points && data.key_points.length > 0 && (
        <CollapsibleSection
          title={`Key Points (${data.key_points.length})`}
          icon={Lightbulb}
          section="keyPoints"
        >
          <ul className="space-y-2">
            {data.key_points.map((point: any, index: number) => (
              <li key={index} className="flex gap-3 items-start">
                <span className="text-blue-600 font-bold mt-0.5">{index + 1}.</span>
                <span className="text-gray-700">{point.point}</span>
              </li>
            ))}
          </ul>
        </CollapsibleSection>
      )}

      {/* Timestamped Analysis */}
      {data.timestamped_analysis && data.timestamped_analysis.length > 0 && (
        <CollapsibleSection
          title={`Timestamped Analysis (${data.timestamped_analysis.length} segments)`}
          icon={Clock}
          section="timestampedAnalysis"
        >
          <div className="space-y-4">
            {data.timestamped_analysis.map(
              (segment: any, index: number) => (
                <div
                  key={index}
                  className="p-3 bg-blue-50 rounded-lg border border-blue-200"
                >
                  <div className="flex justify-between items-start mb-2">
                    <h4 className="font-semibold text-gray-900">
                      Segment {segment.segment_number}
                    </h4>
                    <span className="text-sm text-gray-600">
                      {formatTime(segment.timestamp)}
                    </span>
                  </div>
                  <p className="text-gray-700 mb-2">{segment.summary}</p>
                  {segment.key_insights && segment.key_insights.length > 0 && (
                    <div className="mt-2 pl-4 border-l-2 border-blue-300">
                      <p className="text-sm font-medium text-gray-600 mb-1">
                        Key Insights:
                      </p>
                      <ul className="text-sm text-gray-700 space-y-1">
                        {segment.key_insights.map(
                          (insight: string, idx: number) => (
                            <li key={idx} className="list-disc list-inside">
                              {insight}
                            </li>
                          )
                        )}
                      </ul>
                    </div>
                  )}
                </div>
              )
            )}
          </div>
        </CollapsibleSection>
      )}

      {/* Captions */}
      {data.captions && data.captions.length > 0 && (
        <CollapsibleSection
          title={`Captions (${data.captions.length} segments)`}
          icon={FileText}
          section="captions"
        >
          <div className="space-y-2 max-h-96 overflow-y-auto">
            {data.captions.map((caption: any, index: number) => (
              <div
                key={index}
                className="p-2 bg-gray-50 rounded text-sm flex justify-between items-start gap-2"
              >
                <div className="flex-1">
                  <span className="text-gray-500 font-mono">
                    {formatTime(caption.timestamp)}
                  </span>
                  <p className="text-gray-700 mt-1">{caption.text}</p>
                </div>
                <button
                  onClick={() => handleCopy(caption.text, `caption-${index}`)}
                  className="p-1 hover:bg-gray-200 rounded transition flex-shrink-0"
                  title="Copy caption"
                >
                  {copiedIndex === `caption-${index}` ? (
                    <Check className="w-4 h-4 text-green-600" />
                  ) : (
                    <Copy className="w-4 h-4 text-gray-400" />
                  )}
                </button>
              </div>
            ))}
          </div>
        </CollapsibleSection>
      )}

      {/* Processing Info */}
      {data.processing_time && (
        <div className="p-3 bg-green-50 border border-green-200 rounded-lg text-sm text-gray-600">
          <span className="font-medium">Processing completed in</span> {data.processing_time}s
        </div>
      )}
    </div>
  );
}
