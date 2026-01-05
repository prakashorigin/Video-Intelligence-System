'use client';

import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { analyzeVideo } from '@/lib/api';
import { Play, Loader2, AlertCircle, CheckCircle2 } from 'lucide-react';

const VideoAnalysisSchema = z.object({
  url: z.string().url('Please enter a valid YouTube URL').min(1, 'URL is required'),
});

type VideoAnalysisForm = z.infer<typeof VideoAnalysisSchema>;

interface AnalysisState {
  loading: boolean;
  data: any | null;
  error: string | null;
}

export function VideoAnalyzer() {
  const [analysis, setAnalysis] = useState<AnalysisState>({
    loading: false,
    data: null,
    error: null,
  });

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<VideoAnalysisForm>({
    resolver: zodResolver(VideoAnalysisSchema),
  });

  const onSubmit = async (data: VideoAnalysisForm) => {
    setAnalysis({ loading: true, data: null, error: null });

    try {
      const result = await analyzeVideo(data.url);
      
      if (result.success) {
        setAnalysis({ loading: false, data: result, error: null });
        reset();
      } else {
        setAnalysis({
          loading: false,
          data: null,
          error: result.message || 'Analysis failed',
        });
      }
    } catch (error: any) {
      const errorMessage = error.detail || error.message || 'Failed to analyze video';
      setAnalysis({ loading: false, data: null, error: errorMessage });
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4 md:p-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex justify-center mb-4">
            <div className="bg-gradient-to-br from-blue-600 to-indigo-600 rounded-full p-3">
              <Play className="w-8 h-8 text-white" />
            </div>
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-3">
            Video Intelligence System
          </h1>
          <p className="text-lg text-gray-600">
            Extract captions, summaries, and insights from YouTube videos using AI
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Input Section */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Analyze Video</h2>
              
              <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    YouTube URL
                  </label>
                  <input
                    type="text"
                    placeholder="https://youtube.com/watch?v=..."
                    {...register('url')}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
                    disabled={analysis.loading}
                  />
                  {errors.url && (
                    <p className="text-red-500 text-sm mt-1">{errors.url.message}</p>
                  )}
                </div>

                <button
                  type="submit"
                  disabled={analysis.loading}
                  className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold py-2 px-4 rounded-lg hover:shadow-lg transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                >
                  {analysis.loading ? (
                    <>
                      <Loader2 className="w-4 h-4 animate-spin" />
                      Analyzing...
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4" />
                      Analyze Video
                    </>
                  )}
                </button>
              </form>

              {/* Error Message */}
              {analysis.error && (
                <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg flex gap-3">
                  <AlertCircle className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" />
                  <p className="text-sm text-red-600">{analysis.error}</p>
                </div>
              )}
            </div>
          </div>

          {/* Results Section */}
          <div className="lg:col-span-2">
            {analysis.data ? (
              <VideoResults data={analysis.data} />
            ) : (
              <div className="bg-white rounded-lg shadow-lg p-8 text-center">
                <div className="text-gray-500">
                  <p className="text-lg font-medium mb-2">No analysis yet</p>
                  <p className="text-sm">Enter a YouTube URL and click "Analyze Video" to get started</p>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
